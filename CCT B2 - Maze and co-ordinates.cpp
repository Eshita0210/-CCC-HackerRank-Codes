#include <iostream>
#include <vector>
#include <stack>
using namespace std;

bool can_reach_end(vector<vector<int>> maze, pair<int, int> start, pair<int, int> end) {
    int n = maze.size();
    int m = maze[0].size();
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    stack<pair<int, int>> s;
    s.push(start);
    while (!s.empty()) {
        int x = s.top().first;
        int y = s.top().second;
        s.pop();
        if (x == end.first && y == end.second) {
            return true;
        }
        visited[x][y] = true;
        int dx[] = {0, 1, 0, -1};
        int dy[] = {1, 0, -1, 0};
        for (int i = 0; i < 4; i++) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            if (new_x >= 0 && new_x < n && new_y >= 0 && new_y < m && !visited[new_x][new_y] && maze[new_x][new_y] <= maze[x][y]) {
                s.push(make_pair(new_x, new_y));
            }
        }
    }
    return false;
}

int main() {
    int n, m;
    cin >> n >> m;
    pair<int, int> start;
    cin >> start.first >> start.second;
    start.first--;
    start.second--;
    pair<int, int> end;
    cin >> end.first >> end.second;
    end.first--;
    end.second--;
    vector<vector<int>> maze(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> maze[i][j];
        }
    }
    if (can_reach_end(maze, start, end)) {
        cout << "Hie Barua" << endl;
    } else {
        cout << "No Chance" << endl;
    }
    return 0;
}
