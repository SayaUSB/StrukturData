#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000;
int n, m;
vector<string> grid;
pair<int, int> start, target;  // Ganti nama dari 'end' ke 'target'
bool visited[MAXN][MAXN];
pair<int, int> parent[MAXN][MAXN];
char moveFromParent[MAXN][MAXN];

vector<pair<int, int>> directions = {
    {-1, 0}, // Up
    {1, 0},  // Down
    {0, -1}, // Left
    {0, 1}   // Right
};
char dirChar[] = {'U', 'D', 'L', 'R'};

bool isValid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m &&
           !visited[x][y] && grid[x][y] != '#';
}

void bfs() {
    queue<pair<int, int>> q;
    q.push(start);
    visited[start.first][start.second] = true;

    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        if (make_pair(x, y) == target) break;

        for (int i = 0; i < 4; i++) {
            int nx = x + directions[i].first;
            int ny = y + directions[i].second;
            if (isValid(nx, ny)) {
                visited[nx][ny] = true;
                parent[nx][ny] = {x, y};
                moveFromParent[nx][ny] = dirChar[i];
                q.push({nx, ny});
            }
        }
    }
}

int main() {
    cin >> n >> m;
    grid.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'A') start = {i, j};
            if (grid[i][j] == 'B') target = {i, j}; // Ganti 'end' jadi 'target'
        }
    }

    bfs();

    if (visited[target.first][target.second]) {
        cout << "YES\n";
        string path;
        pair<int, int> cur = target;
        while (cur != start) {
            path += moveFromParent[cur.first][cur.second];
            cur = parent[cur.first][cur.second];
        }
        reverse(path.begin(), path.end());
        cout << path.size() << "\n" << path << "\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
