using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003520: Duckling
/// </summary>
public class _11003520 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0816160115009021$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009024$
                // - ...
                return -1;
            case (40, 0):
                // $script:0816160115009025$
                // - Quack...?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
