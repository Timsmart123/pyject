def teLoop(inp, datatype = str):
    while True:
        try:
            question = datatype(input(inp))

            if datatype == str and not question.strip():
                raise ValueError

            return question

        except ValueError:
            print("Not Valid")
