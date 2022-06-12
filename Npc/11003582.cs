using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003582: Veliche
/// </summary>
public class _11003582 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1116181907009256$
    // - The future is in our hands.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1127103307011969$
                // - The future is in our hands.
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
