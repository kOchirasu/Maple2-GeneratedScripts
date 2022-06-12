using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000782: Lavor
/// </summary>
public class _11000782 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002948$
    // - I can see a light shining in your eyes. What can I do for you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002951$
                // - Hey there, young $male:fellow,female:lady$. You look like a traveler. I hope you're making the most of your youth and seeing the world. 
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
