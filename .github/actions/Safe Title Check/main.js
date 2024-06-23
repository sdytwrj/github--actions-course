const core = require('@actions/core');

try {
  const prTitle = core.getInput('pr-title');
  if (prTitle.startsWith('feat')) {
    console.log('PR is a feature');
  } else {
    console.log('PR is not a feature');
  }
} catch (error) {
  core.setFailed(`Action failed with error ${error}`);
}
