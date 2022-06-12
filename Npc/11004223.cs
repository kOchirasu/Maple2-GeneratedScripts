using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004223: Rinet
/// </summary>
public class _11004223 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010794$
    // - <font color="#909090">(He glares at you, then down at the clarinet in his mouth, then back at you.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010795$
                // - <font color="#909090">(He glares at you, then down at the clarinet in his mouth, then back at you.)</font>
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
