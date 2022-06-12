using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000567: Injured Guard
/// </summary>
public class _11000567 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 50;60;70;80
    }

    // Select 0:
    // $script:0831180407002345$
    // - Ugh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002350$
                // - H-help... 
                return -1;
            case (60, 0):
                // $script:0831180407002351$
                // - Ugh... 
                return -1;
            case (70, 0):
                // $script:0831180407002352$
                // - Ugh... No... 
                return -1;
            case (80, 0):
                // $script:0831180407002353$
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
