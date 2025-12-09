use std::collections::{HashMap, HashSet};
use std::fs;

fn main() {
    let content = fs::read_to_string("i.txt").expect("Failed to read file");
    let lines: Vec<&str> = content.lines().collect();

    let mut ans = 0i64;

    // Parse points and find part 1 answer
    let mut points: Vec<(i64, i64)> = Vec::new();
    for i in 0..lines.len() {
        let parts: Vec<i64> = lines[i].split(',').map(|x| x.trim().parse().unwrap()).collect();
        let (ax, ay) = (parts[0], parts[1]);
        points.push((ax, ay));
        for j in (i + 1)..lines.len() {
            let parts2: Vec<i64> = lines[j].split(',').map(|x| x.trim().parse().unwrap()).collect();
            let (bx, by) = (parts2[0], parts2[1]);
            let width = (bx - ax).abs() + 1;
            let length = (by - ay).abs() + 1;
            ans = ans.max(width * length);
        }
    }
    println!("{}", ans);

    // 1 == red, 2 == green
    let mut g: HashMap<(i64, i64), i32> = HashMap::new();

    let start = points[0];
    let mut previous: Option<(i64, i64)> = None;

    for &(ax, ay) in &points {
        g.insert((ax, ay), 1);
        if let Some(prev) = previous {
            for greenyi in prev.1.min(ay)..=prev.1.max(ay) {
                for greenxi in prev.0.min(ax)..=prev.0.max(ax) {
                    g.entry((greenxi, greenyi)).or_insert(2);
                }
            }
        }
        previous = Some((ax, ay));
    }

    // Connect last point back to start
    let prev = previous.unwrap();
    for greenyi in start.1.min(prev.1)..=start.1.max(prev.1) {
        for greenxi in start.0.min(prev.0)..=start.0.max(prev.0) {
            g.entry((greenxi, greenyi)).or_insert(2);
        }
    }

    // Precompute edges
    let mut edges: Vec<(i64, i64, i64)> = Vec::new();
    for i in 0..points.len() {
        let p1 = points[i];
        let p2 = points[(i + 1) % points.len()];
        edges.push((p1.1.min(p2.1), p1.1.max(p2.1), p1.0.max(p2.0)));
    }

    // Memoization cache for even_odd_test
    let mut cache: HashSet<(i64, i64)> = HashSet::new();
    for &key in g.keys() {
        cache.insert(key);
    }

    let even_odd_test = |point: (i64, i64), cache: &mut HashSet<(i64, i64)>| -> bool {
        if cache.contains(&point) {
            return true;
        }
        let mut count = 0;
        let (cx, cy) = point;

        for &(y1, y2, x2) in &edges {
            if y1 < cy && cy <= y2 {
                if cx < x2 {
                    count += 1;
                }
            }
        }

        let inside = count % 2 == 1;
        if inside {
            cache.insert(point);
        }
        inside
    };

    ans = 0;

    for i in 0..points.len() {
        let (ax, ay) = points[i];
        for j in (i + 1)..points.len() {
            let (bx, by) = points[j];
            let width = (bx - ax).abs() + 1;
            let length = (by - ay).abs() + 1;
            let t = width * length;
            if t <= ans {
                continue;
            }

            // Check corners first
            let corners = [(ax, ay), (ax, by), (bx, ay), (bx, by)];
            let mut corner_fail = false;
            for &c in &corners {
                if !even_odd_test(c, &mut cache) {
                    corner_fail = true;
                    break;
                }
            }
            if corner_fail {
                continue;
            }

            let mut fail = false;
            for py in ay.min(by)..=ay.max(by) {
                if !even_odd_test((ax, py), &mut cache) {
                    fail = true;
                    break;
                }
                if !even_odd_test((bx, py), &mut cache) {
                    fail = true;
                    break;
                }
            }
            if fail {
                continue;
            }

            for px in ax.min(bx)..=ax.max(bx) {
                if !even_odd_test((px, ay), &mut cache) {
                    fail = true;
                    break;
                }
                if !even_odd_test((px, by), &mut cache) {
                    fail = true;
                    break;
                }
            }
            if fail {
                continue;
            }

            if t > ans {
                ans = t;
                println!("New ans: {}", ans);
            }
            ans = ans.max(width * length);
        }
    }
    println!("{}", ans);
}
