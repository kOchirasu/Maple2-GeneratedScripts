using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000054: Luke
/// </summary>
public class _11000054 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000232$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000235$
                // - Bah! $npcName:11000062[gender:1]$ said she would go attend the court with her dad. Why isn't my gramps saying anything? I want to go to see the empress too!
                return -1;
            case (40, 0):
                // $script:0831180407000236$
                // - $npcName:11000056[gender:0]$ knows about a lot of things. If you have questions, you should ask him!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
