using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004230: Ruche
/// </summary>
public class _11004230 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010810$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010811$
                // - <font color='#909090'>(The fox tilts its head inquisitively.)</font>
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
