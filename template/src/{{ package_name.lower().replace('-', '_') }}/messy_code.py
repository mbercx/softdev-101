def calculate_statistics(data,include_median=True):
    """Calculate statistics for a list of numbers."""
    debug_mode=True
    if len(data)==0:
        return None

    mean=sum(data)/len(data)
    result={'mean':mean,'min':min(data),'max':max(data)}

    if include_median:
        sorted_data=sorted(data)
        n=len(sorted_data)
        median=sorted_data[n//2] if n%2!=0 else (sorted_data[n//2-1]+sorted_data[n//2])/2
        result['median']=median

    return result