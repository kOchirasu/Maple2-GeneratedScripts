using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000492: Nelph
/// </summary>
public class _11000492 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407002158$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002161$
                // - I've spoken with many people who are frustrated that the court will not be held.
                switch (selection) {
                    // $script:0831180407002162$
                    // - It must be difficult to explain it to every single person.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002163$
                // - It certainly is, but I understand their frustration. They came all the way here to attend the court, only to have their plans ruined. They're upset and disappointed.
                return 31;
            case (31, 1):
                // $script:0831180407002164$
                // - Whatever the reason, I still feel personally responsible since I was the one charged with the preparations.
                return -1;
            case (40, 0):
                // $script:0831180407002165$
                // - My job is to make sure $npcName:11000075[gender:1]$ and the other members of the royal family have everything they need for their day. I'm always busy, but I take pride in my position and my service to $map:02000025$.
                return -1;
            case (50, 0):
                // $script:0831180407002166$
                // - Have you been to $map:02000076$? My mother lives there. I really should visit her, but I've been so busy that I haven't had the time since preparations began. 
                return 50;
            case (50, 1):
                // $script:0831180407002167$
                // - Once my work here is done and I've sorted out all the issues, I'll go and visit her first thing! I've been sending her letters, it's just... she can't see. A disease took her eyesight. Sigh... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
