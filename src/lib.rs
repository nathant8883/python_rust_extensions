use pyo3::{pyfunction, pymodule, PyResult, Python, wrap_pyfunction};
use pyo3::prelude::PyModule;

#[pyfunction]
fn say_hello() {
    println!("Hello, world!");
}

#[pymodule]
fn python_extensions_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(say_hello));
    Ok(())
}

