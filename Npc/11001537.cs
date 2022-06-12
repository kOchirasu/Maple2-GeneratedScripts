using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001537: Ipigio
/// </summary>
public class _11001537 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0322222107005986$
    // - Sh! You'll give me away! 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0329103507006001$
                // - How did you find me...?
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
