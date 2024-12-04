example of how to use react components with streamlit

# How To

1. `cd custom_components`
2. `npm create vite@latest`
3. select react (typescript, no swc)
4. `cd <name>`
5. `npm i`
6. `npm i streamlit-component-lib`
7. Go to `vite.config.ts`
8. Add `base: "./"` to `defineConfig`
9. (OPTIONAL) add a server port for dev environment
10. Decide wether you want one `__init__.py` per component or one for all components (see [init.py](#__init__py) for what i mean)
11. Edit your Component as classes (!)
12. Make sure to provide the right path etc in your init.py of choice
13. Use in your streamlit app.

> There is one example (Table) where you have a sub-folder `frontend` for your react code, and one where you don't (Counter). See what fits you best (or find your own) and continue that way.

❗ To see how to make things reactive, see the Counter example❗

## `__init__.py`

- One for all: Everything at one place
- One for each: easier dev-setup
