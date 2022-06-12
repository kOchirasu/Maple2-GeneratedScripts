using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004191: Holstatt
/// </summary>
public class _11004191 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0813101707010950$
    // - Huh?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0813101707010951$
                // - I am sorry for misleading you. But surely you must see that I had no choice.
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
