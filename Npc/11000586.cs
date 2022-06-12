using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000586: Injured Guard
/// </summary>
public class _11000586 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 50;60;70;80
    }

    // Select 0:
    // $script:0831180407002370$
    // - Ugh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002375$
                // - H-help... 
                return -1;
            case (60, 0):
                // $script:0831180407002376$
                // - Ugh... 
                return -1;
            case (70, 0):
                // $script:0831180407002377$
                // - Ugh... No... 
                return -1;
            case (80, 0):
                // $script:0831180407002378$
                // - I can't... die like this... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            (80, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
