using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000936: Duna
/// </summary>
public class _11000936 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1121222006000857$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1121222006000858$
                // - Can I help you?
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
