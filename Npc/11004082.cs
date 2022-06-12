using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004082: Frightened Shut-In
/// </summary>
public class _11004082 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010273$
    // - Sigh... Will I ever get to leave this house again?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010274$
                // - Sigh... Will I ever get to leave this house again?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
