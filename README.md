# Public Performance Testing Guide

## Dependencies:

- **`resources/issuers_example.csv`**: Accessible Payer Testing Accounts which have both public and private keys.
- **`resources/accounts_example.csv`**: Payer's public address in `issuers_example.csv` that have first and second half swapped.

We have provided 2 JMX files for IOU-IOU testing and XRP-XRP testing inside the `jmx_file` directory.

## Testing Instructions

### XRP-XRP Testing

To launch the XRP-XRP testing, run the following command:

```shell
apache-jmeter-5.4.3/bin/jmeter -n -t jmx_file/xrp2xrp.jmx -j <jmeter.log> -l <jmeter.csv>
```

### AMM/Orderbook Testing

To launch the AMM/orderbook testing, run:

```shell
apache-jmeter-5.4.3/bin/jmeter -n -t jmx_file/payment_IOUIOU_mixLoad.jmx -j <jmeter.log> -l <jmeter.csv>
```

## Customization

To customize the parameters, please modify the `apache-jmeter-5.4.3/bin/user.properties` file with the following settings:

- **Number_of_threads**: Number of concurrent threads for testing.
- **Ramp_up_time**: Duration to gradually increase the number of active threads.
- **Duration**: Total test duration in seconds.
- **Duration_ledger**: Duration in seconds for ledger monitoring.
- **Payer**: Path to your payers file.
- **Payee**: Path to your payee file.
- **resource_dir**: Directory where the CSV files are located, relative to your command running directory.

## Additional Resource Files

- **`IOU_owner.csv`**: The issuer of the trustline for IOU currency.
- **`lp.csv`**: The liquidity provider for the orderbook or AMM object.

*Note: For optimal testing results, it is advised to establish a synthetic database populated with IOU tokens for AMM testing. The provided JMX scripts are designed based on a simplified topology where IOU tokens are assumed to be held by a single account, and the AMM liquidity is managed by another distinct account. (For detailed test setup, please visit: https://engineering.ripple.com/amm-performance-testing-report/ *

## Ledger Monitoring

Each JMX file includes a ledger monitoring script. During performance testing, this script will collect information for each validated ledger. The details are then recorded in the `jmeter.log` file as specified by you. This monitoring process will be active and running concurrently with the performance tests, ensuring comprehensive data collection and analysis throughout the testing period.

## Report Generation

Run the following command to generate a HTML based test report from the test result file you've specified (`jmeter.csv`) during test startup:

```shell
apache-jmeter-5.4.3/bin/jmeter -g <jmeter.csv> -o <jmeter_report_dir_name>
```

## Further Reading

- [Apache JMeter Documentation](https://jmeter.apache.org/)
- [AMM Performance Testing Report](https://engineering.ripple.com/amm-performance-testing-report/)




