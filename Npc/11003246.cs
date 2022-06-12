using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003246: Frey
/// </summary>
public class _11003246 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008152$
    // - $MyPCName$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008153$
                // - In times like this, you need to keep your wits about you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
