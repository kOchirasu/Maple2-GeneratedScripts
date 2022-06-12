using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004413: Frosty Fairfolk
/// </summary>
public class _11004413 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1120173007011877$
    // - Come visit $map:63000072$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1120173007011880$
                // - $map:63000072$ is bursting with joyous holiday cheer! People are happy! Fairfolk are happy! And it's SNOWING!!
                return 10;
            case (10, 1):
                // $script:1120173007011881$
                // - Board this toy train if you want to go to $map:63000072$! Toot, toot!
                return 10;
            case (10, 2):
                // $script:1120173007011882$
                // - The toy train is completely free because it's run by the fairfolk! We barely even know what money is! Come along to $map:63000072$!
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
