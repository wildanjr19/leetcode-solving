import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    results = activity.sort_values(by='event_date').groupby('player_id').head(1)
    results = results.drop(columns=['device_id', 'games_played'])
    results = results.rename(columns={'event_date' : 'first_login'})
    return results