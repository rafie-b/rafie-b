import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    "user_id": ["A1", "A1", "A2", "A2", "A3", "A4", "A4", "A5", "A5", "A5", "A2"],
    "game_id": ["G1", "G1", "G1", "G1", "G1", "G2", "G2", "G2", "G2", "G2", "G3"],
    "bet": [50, 100, 50, 75, 25, 10, 20, 30, 40, 50, 200],
    "won": [50, 0, 0, 75, 0, 15, 0, 0, 0, 100, 300],
    "timestamp": ["2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05",
                  "2021-02-01", "2021-02-02", "2021-02-03", "2021-02-04", "2021-02-05", "2021-02-05"]
})

def aggregate_game_data(df: pd.DataFrame, n: int) -> dict:
    # create an empty dictionary to store game data
    game_data = {}
    # loop over unique game IDs
    for game_id in df['game_id'].unique():
        # filter the DataFrame to only include data for the current game_id
        game_df = df[df['game_id'] == game_id]
        # calculate the max bet per user_id
        max_bet_per_user = game_df.groupby('user_id')['bet'].max()
        # calculate the average bet per user_id and round down to the nearest integer
        avg_bet_per_user = game_df.groupby('user_id')['bet'].mean().astype(int)
        # get the top n user_ids by bet sum
        top_n_user_ids = game_df.groupby('user_id')['bet'].sum().nlargest(n).index.tolist()
        # if n is greater than the number of unique user_ids, return all user_ids
        if n > len(game_df['user_id'].unique()):
            top_n_user_ids = game_df.groupby('user_id')['bet'].sum().nlargest(len(game_df['user_id'].unique())).index.tolist()
        # add the game data to the dictionary
        game_data[game_id] = {
            "max_bet": max_bet_per_user.max(),
            "avg_bet": avg_bet_per_user.min(),
            "top_n_user_ids": top_n_user_ids
        }
    return game_data

# assuming you have already loaded your DataFrame "df"
n = 5 # the value of n, as per the prompt
game_data = aggregate_game_data(df, n)
print(game_data)