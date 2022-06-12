using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000530: Schwanda
/// </summary>
public class _11000530 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407002276$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002277$
                // - I mostly paint portraits. Would you like to know why?
                return 10;
            case (10, 1):
                // $script:0831180407002278$
                // - Because the most beautiful thing in the world is people! That's why I like painting them. 
                return -1;
            case (20, 0):
                // $script:0831180407002279$
                // - Would you like to know when I started painting?
                return 20;
            case (20, 1):
                // $script:0831180407002280$
                // - Well, that's... I don't know. Do you remember when you started eating food on your own? Or when you spoke your first word?
                return 20;
            case (20, 2):
                // $script:0831180407002281$
                // - Picking up a brush was as natural to me as picking up a spoon. I was born to paint. I don't need to know exactly when I started doing it.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
