class DataQualityService:
    def null_check(self, df, cols):
        return df[cols].notnull().all().all()

    def duplicate_check(self, df, keys):
        return df.duplicated(subset=keys).sum()

    def threshold_check(self, df, col, min_val=0):
        return (df[col] >= min_val).all()
