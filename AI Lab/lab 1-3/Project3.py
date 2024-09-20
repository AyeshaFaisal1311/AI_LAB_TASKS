import pandas as pd

df=pd.DataFrame([
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
],columns=["Movie","Budget"])

def add(df):
    num_movies_add=int(input("How many movies you want to add?"))
    try:
       num_movies_add=int(num_movies_add)
       if num_movies_add<=0:
          print("Enter +ve integer")
          return
    except ValueError:
       print("Invalid input")
       return
    
    for movie_index in range(num_movies_add):
       movie_name = input("Enter name of movie: ")
       while True :
        movie_budget=int(input("Enter budget of movie"))

        try:
          movie_budget=int(movie_budget)
          if movie_budget<0:
             print("Budget cannot be -ve")
             continue
          break
        except ValueError:
                print("Invalid input")
                continue
        new_row=pd.DataFrame([{"Movie":movie_name,"Budget":movie_budget}])       
        df=pd.concat([df,new_row],ignore_index
                     =True)
    return df

def calculate_average(df):
    average_budget = df['Budget'].mean()
    return average_budget

def high_budget(df,average_budget):
    high_budget_movies = df[df['Budget'] > average_budget]
    return high_budget_movies

def main():
    global df
    add_more_movie=input("Do you want to enter more movies?")
    if add_more_movie.lower() == "yes":
        df=add(df)
        average_budget=calculate_average(df)
        high_budget_movies=high_budget(df,average_budget)
        print("Average Budget: ", average_budget)
        print("High_budget_movies:",high_budget_movies)

if __name__=='__main__':
   main()

