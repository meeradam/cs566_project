def recommend_friends_with_bfs( adjacency_list, user):
    # Get the BFS traversal from the existing function
    bfs_result = bfs(adjacency_list, user)
    
    # Collect direct friends
    direct_friends = set(adjacency_list.get(user, []))
    
    # Recommendations dictionary
    recommendations = {}

    # Iterate over BFS results
    for friend in bfs_result:
        if friend not in direct_friends and friend != user:
            # Count mutual friends
            mutual_friends = len(direct_friends & set(adjacency_list.get(friend, [])))
            recommendations[friend] = mutual_friends

    # Sort recommendations by the number of mutual friends (descending)
    return sorted(recommendations.items(), key=lambda x: -x[1])

# Example Usage
