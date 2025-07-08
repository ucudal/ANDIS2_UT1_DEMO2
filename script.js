import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 10,
    duration: '30s',
    thresholds: {
        http_req_duration: ['p(95)<1000']
    },
};
export default function () {
    http.get('http://127.0.0.1:5001/saludo');
    sleep(1);
}