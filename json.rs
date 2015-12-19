extern crate rustc_serialize;

use rustc_serialize::json::Json;

fn parser_test() {
    let doc = r#"{
        "name": "bibhas",
        "num1": -10.0,
        "objItem": {
            "num2": -10,
            "arrayItem2": [40, 50, 60]
        }
    }"#;

    match getname(doc) {
        Ok(name) => println!("Name is: {}", name),
        Err(e) => println!("{}", e),
    }
}

fn getname(doc: &str) -> Result<String, String> {
    let json = try!(Json::from_str(doc).map_err(|e| format!("Failed to parse JSON: {}", e)));
    let root = try!(json.as_object().ok_or("Root is not an object."));
    let name_field = try!(root.get("name").ok_or("No field 'name'."));
    let name = try!(name_field.as_string().ok_or("Field 'name' is not a string."));
    Ok(name.to_owned())
}

fn main() {
    parser_test();
}
