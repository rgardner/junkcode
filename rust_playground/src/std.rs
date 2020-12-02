#[cfg(test)]
mod tests {
    #[test]
    fn test_option_string_unwrap_or_default_when_called_on_empty_string_returns_empty_string() {
        let opt: Option<String> = None;
        let actual = opt.unwrap_or_default();
        assert_eq!(actual, "".to_string());
    }

    #[test]
    fn test_option_string_filter_when_called_with_true_returns_none() {
        let opt = Some("".to_string());
        let actual = opt.filter(|s| !s.is_empty());
        assert_eq!(actual, None);
    }
}
