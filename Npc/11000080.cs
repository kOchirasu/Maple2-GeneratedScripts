using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000080: Mimi
/// </summary>
public class _11000080 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000368$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000371$
                // - This place is connected to $map:02000001$ by the great Royal Road. Just stay on it, and you'll be there in no time.
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
