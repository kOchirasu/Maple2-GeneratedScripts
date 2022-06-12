using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004024: Bjorn
/// </summary>
public class _11004024 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010035$
    // - I haven't given up yet.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010036$
                // - I will restore my kingdom.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
