import { ExpoRoot } from 'expo-router';
import 'expo-router/entry';

export default function App() {
	const ctx = require.context('./src/app');
	return <ExpoRoot context={ctx} />;
}
