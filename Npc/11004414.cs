using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004414: Frosty Fairfolk
/// </summary>
public class _11004414 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1120173007011883$
    // - Don't you want to taste a fairfolk cake?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1120173007011886$
                // - There are many people who hunger for the fairfolk's cake. But it seems no two people have the same reaction to it! Isn't that interesting?
                return 10;
            case (10, 1):
                // $script:1120173007011887$
                // - Some say it has no taste, others claim it's the most flavorful food they've ever eaten. Maybe it simply causes madness?
                return 10;
            case (10, 2):
                // $script:1120173007011888$
                // - In any event, try some! Go on, eat it up!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
