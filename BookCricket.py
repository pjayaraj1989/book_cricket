from Resources import*

if __name__ == "__main__":
    balls=10
    sachin=Player('Sachin',False, 0, 0)
    sehwag=Player('Sehwag',False, 0, 0)

    #first member always on strike
    pair = [sachin, sehwag]
    sachin.onstrike=True

    Play(pair)
