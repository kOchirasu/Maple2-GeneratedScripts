using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001495: Startz
/// </summary>
public class _11001495 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0118150907005816$
    // - Do you need more food?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0118150907005819$
                // - I've got a bad feeling... like something bad's about to happen.
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
