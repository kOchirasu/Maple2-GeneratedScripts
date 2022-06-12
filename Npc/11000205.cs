using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000205: Lily
/// </summary>
public class _11000205 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1121222006000801$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1121222006000802$
                // - What is it?
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
