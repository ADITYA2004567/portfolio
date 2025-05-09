from datetime import datetime

def calculate_stage(time):
    hiring_stages = [
        'Application Submitted',
        'Application Reviewed',
        'Screening Call Scheduled',
        'Screening Call Completed',
        'Interview Scheduled',
        'Interview Completed',
        'Offer Extended',
        'Offer Accepted',
        'Onboarding Started'
    ]
    durations = {}
    x = list(time.keys())
    for i in range(len(x) - 1):
        s = x[i]
        next_stage = x[i + 1]
        durations[s] = {
            'stage': hiring_stages[i],
            'duration': time[next_stage] - time[s],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    total_time = sum(time[next_stage] - time[s] for s, next_stage in zip(x, x[1:]))
    durations['total_time_spent'] = total_time

    for stage, info in durations.items():
        if stage != 'total_time_spent':
            print(f"Stage: {info['stage']}, Duration: {info['duration']} seconds, Timestamp: {info['timestamp']}")
    print(f"Total Time Spent: {total_time} seconds")
    return durations

time_stamps = {
    'application_submitted': 0,
    'application_reviewed': 6600,
    'screening_call_scheduled': 7200,
    'screening_call_completed': 10800,
    'interview_scheduled': 4400,
    'interview_completed': 8000,
    'offer_extended': 21600,
    'offer_accepted': 25200,
    'onboarding_started': 28800
}

calculate_stage(time_stamps)