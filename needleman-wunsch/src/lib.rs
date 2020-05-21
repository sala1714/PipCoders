use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use std::cmp::max;

#[pyfunction]
fn maximum_score(mut secuence_a: String, mut secuence_b: String) -> PyResult<i16> {
    secuence_a = str::replace(&secuence_a, "R", "G");
    secuence_a = str::replace(&secuence_a, "Y", "T");
    secuence_a = str::replace(&secuence_a, "K", "G");
    secuence_a = str::replace(&secuence_a, "M", "A");
    secuence_a = str::replace(&secuence_a, "S", "G");
    secuence_a = str::replace(&secuence_a, "W", "A");
    secuence_a = str::replace(&secuence_a, "B", "G");
    secuence_a = str::replace(&secuence_a, "D", "G");
    secuence_a = str::replace(&secuence_a, "H", "A");
    secuence_a = str::replace(&secuence_a, "V", "G");
    secuence_a = str::replace(&secuence_a, "N", "A");

    secuence_b = str::replace(&secuence_b, "R", "G");
    secuence_b = str::replace(&secuence_b, "Y", "T");
    secuence_b = str::replace(&secuence_b, "K", "G");
    secuence_b = str::replace(&secuence_b, "M", "A");
    secuence_b = str::replace(&secuence_b, "S", "G");
    secuence_b = str::replace(&secuence_b, "W", "A");
    secuence_b = str::replace(&secuence_b, "B", "G");
    secuence_b = str::replace(&secuence_b, "D", "G");
    secuence_b = str::replace(&secuence_b, "H", "A");
    secuence_b = str::replace(&secuence_b, "V", "G");
    secuence_b = str::replace(&secuence_b, "N", "A");

    let a: Vec<char> = secuence_a.chars().collect();
    let b: Vec<char> = secuence_b.chars().collect();

    let mut f: Vec<i16> = vec![0;(b.len() + 1) * (a.len() + 1)];
    for i in 0..(b.len() + 1) {
        f[i*(a.len() + 1)] = i as i16 * -1;
    }
    for j in 0..(a.len() + 1) {
        f[j] = j as i16* -1;
    }

    for i in 1..(b.len() + 1) {
        for j in 1..(a.len() + 1) {
            let mut is_match = 0;
            if a[j - 1] == b[i - 1] {
                is_match = f[(i-1)*(a.len() + 1) + (j - 1)] + 1;
            } else {
                is_match = f[(i-1)*(a.len() + 1) + (j - 1)] - 1;
            }
            let is_delete = f[(i-1)*(a.len() + 1) + (j)] - 1;
            let is_insert = f[(i)*(a.len() + 1) + (j - 1)] - 1;
            let maximum = max(max(is_match, is_delete ), is_insert);
            f[(i)*(a.len() + 1) + (j)] = maximum;
        }
    }
    Ok(f[(b.len())*(a.len() + 1) + (a.len())])
}

#[pymodule]
fn needleman_wunsch(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(maximum_score))?;
    Ok(())
}