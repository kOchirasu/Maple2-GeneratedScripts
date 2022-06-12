using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003431: Rutatimo Karr
/// </summary>
public class _11003431 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008649$
    // - It can't be... I lost...?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008650$
                // - It can't be... I lost...?
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
