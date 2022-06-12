using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000491: Cathy Catalina
/// </summary>
public class _11000491 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;70;80
    }

    // Select 0:
    // $script:0831180407002150$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002153$
                // - Right now, Goldus Group is the biggest company in $map:02000100$, but that'll soon change. I'll be crushing $npcName:11000252[gender:0]$ under my heel before you know it.
                return -1;
            case (40, 0):
                // $script:0831180407002154$
                // - What? You want to know if I'm single?
                return 40;
            case (40, 1):
                // $script:0831180407002155$
                // - Hah! I don't need a man. All men are narcissistic, chauvinist pigs. I hate them!
                return -1;
            case (70, 0):
                // $script:0831180407002156$
                // - Can't you see I'm busy? If it's not urgent, then scram.
                return -1;
            case (80, 0):
                // $script:0831180407002157$
                // - I don't sell anything on credit. I trust money more than I trust people.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            (80, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
