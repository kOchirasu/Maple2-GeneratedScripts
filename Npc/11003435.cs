using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003435: Asimov
/// </summary>
public class _11003435 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0726013907008728$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0726013907008729$
                // - ...
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
