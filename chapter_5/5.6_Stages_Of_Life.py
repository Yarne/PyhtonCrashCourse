def determine_stage(age):
    if age < 2:
        stage = 'baby'
        determiner = 'a'
    elif age < 4:
        stage = 'toddler'
        determiner = 'a'
    elif age < 13:
        stage = 'kid'
        determiner = 'a'
    elif age < 20:
        stage = 'teenager'
        determiner = 'a'
    elif age < 65:
        stage = 'adult'
        determiner = 'an'
    else:
        stage = 'elder'
        determiner = 'an'

    print(f"You're {determiner} {stage}.")


stages_of_life = [1, 3, 9, 15, 45, 76]

for stage_of_life in stages_of_life:
    determine_stage(stage_of_life)
