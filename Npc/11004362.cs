using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004362: Aiden
/// </summary>
public class _11004362 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011773$
    // - I never would have imagined that thing was real...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011774$
                // - Life is full of surprises. Case in point, that creature in our living room, celebrating with us...
                return 10;
            case (10, 1):
                // $script:1120173007011851$
                // - ...I guess I could get used to this.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
