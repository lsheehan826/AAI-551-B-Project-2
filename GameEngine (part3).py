def moveRabbits(self):
    for rabbit in self._num_of_rabbits:
        current_x, current_y = rabbit.get_x(), rabbit.get_y()
        move_in_direction = random.choice(['up', 'down', 'left', 'right'])
        new_x, new_y = current_x, current_y
        if move_in_direction == 'up':
            new_y -= 1
        elif move_in_direction == 'down':
            new_y += 1
        elif move_in_direction == 'left':
            new_x -= 1
        elif move_in_direction == 'right':
            new_x += 1

        if 0 <= new_x < len(self._field[0]) and 0 <= new_y < len(self._field):
            if any((new_x == r.get_x() and new_y == r.get_y()) or (
                    new_x == self._captain_object.get_x() and new_y == self._captain_object.get_y()) for r in
                   self._num_of_rabbits):
                continue

            for veggie in self._possible_veggies:
                if veggie and new_x == veggie.get_x() and new_y == veggie.get_y():
                    self._field[current_y][current_x] = None

                    self._field[new_y][new_x] = rabbit

                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)

                    self._field[current_y][current_x] = None
                    break

                else:
                    self._field[current_y][current_x] = None
                    self._field[new_y][new_x] = rabbit
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)


def moveCptVertical(self, vertical_movement):
    current_x, current_y = self._captain_object.get_x(), self._captain_object.get_y()
    new_y = current_y + vertical_movement

    if 0 <= new_y < len(self._field):
        if not self._field[new_y][current_x]:
            self._field[current_y][current_x] = None
            self._field[new_y][current_x] = self._captain_object
            self._captain_object.set_y(new_y)
        else:
            if isinstance(self._field[new_y][current_x], Veggie):
                veggie = self._field[new_y][current_x]

                print(f"Yummy! A delicious {veggie} found")

                self._captain_object.add_veggie(veggie)
                self._score += veggie.get_points_worth()

                self._field[current_y][current_x] = None
                self._field[new_y][current_x] = self._captain_object
                self._captain_object.set_y(new_y)

            elif isinstance(self._field[new_y][current_x], Rabbit):
                print("Don't step on the bunnies!")

        self._field[current_y][current_x] = None


def moveCptHorizontal(self, horizontal_movement):
    current_x, current_y = self._captain_object.get_x(), self._captain_object.get_y()
    new_x = current_x + horizontal_movement

    if 0 <= new_x < len(self._field[0]):
        if not self._field[current_y][new_x]:
            self._field[current_y][current_x] = None
            self._field[current_y][new_x] = self._captain_object
            self._captain_object.set_x(new_x)

        else:
            if isinstance(self._field[current_y][new_x], Veggie):
                veggie = self._field[current_y][new_x]

                print(f"Yummy! A delicious {veggie} found")
                self._captain_object.add_veggie(veggie)
                self._score += veggie.get_points_worth()

                self._field[current_y][current_x] = None
                self._field[current_y][new_x] = self._captain_object
                self._captain_object.set_x(new_x)

            elif isinstance(self._field[current_y][new_x], Rabbit):
                print("Don't step on the bunnies! ")

        self._field[current_y][current_x] = None


def moveCaptain(self):
    direction = input("Would you like to move up(W), down(S), left(A) or right(D)?").lower()

    if direction == 'w':
        self.moveCptVertical(-1)
    elif direction == 's':
        self.moveCptVertical(1)
    elif direction == 'a':
        self.moveCptHorizontal(-1)
    elif direction == 'd':
        self.moveCptHorizontal(1)
    else:
        print(f"{direction} is not a valid option")


def gameOver(self):
    print("GAME OVER!")

    veggies_harvested = self._captain_object.get_veggie_list()
    if veggies_harvested:
        print("You managed to harvest the following vegetables:")
        for veggie in veggies_harvested:
            print(f" -{veggie.get_name()}")
    else:
        print("You did not harvest any vegetables.")

    print(f"Your score was: {self._score}")


def highScore(self):
    high_scores = []

    try:
        with open(self.__HIGHSCOREFILE, 'rb') as file:
            high_scores = pickle.load(file)
    except FileNotFoundError:
        pass

    player_initials = input("Please enter your three initials to go on the scoreboard: ").upper()[:3]
    score_of_player = (player_initials, self._score)

    if not high_scores:
        high_scores.append(score_of_player)

    else:
        added_score = False
        for i, (player_initial, score) in enumerate(high_scores):
            if self._score > score:
                high_scores.insert(i, score_of_player)
                added_score = True
                break

        if not added_score:
            high_scores.append(score_of_player)

    print("HIGH SCORES")
    for player_initial, score in enumerate(high_scores, start=1):
        print(f"{player_initial}   {score}")

    with open(self.__HIGHSCOREFILE, 'wb') as file:
        pickle.dump(high_scores, file)
