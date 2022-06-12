using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000874: Cheyong
/// </summary>
public class _11000874 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407003159$
    // - Ahem... What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407003165$
                // - I don't know if I could handle seeing something like that again. It was surreal, horrifying, futile... 
                switch (selection) {
                    // $script:0831180407003166$
                    // - What are you talking about?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831180407003167$
                // - Are you new to $map:02000111$? Because most people who live here know what I'm talking about. It was the $npcName:23000017$ Tsunami.
                switch (selection) {
                    // $script:0831180407003168$
                    // - Never heard of it.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0831180407003169$
                // - That happened way back when I still had a full head of hair. It was January 23rd, around 11 p.m. The cold, merciless wind was churning the sea when the legendary turtle king $npcName:23000017$ awoke and rose to the ocean's surface from his briny domain.
                return 12;
            case (12, 1):
                // $script:0831180407003170$
                // - I've never seen such a massive, terrifying creature in my whole life. And it was fast. I couldn't believe it was a turtle. 
                return 12;
            case (12, 2):
                // $script:0831180407003171$
                // - Anyway, the news of the legendary turtle king surfacing quickly spread, and great warriors came from all over Maple World to battle back the deadliest turtle in history. Ahhh, just recalling that day makes my nonexistent hair stand on end.
                return 12;
            case (12, 3):
                // $script:0831180407003172$
                // - A single strike from that turtle's leg sent dozens of warriors flying. Some of them were terrified into running. But enough brave souls stuck it out to tire the turtle out. For awhile, it looked like we might come out on top.
                return 12;
            case (12, 4):
                // $script:0831180407003173$
                // - It must have been an hour into the battle, when suddenly a loud roar came up from the sea. The next thing I remember is someone screaming about a tsunami coming.
                return 12;
            case (12, 5):
                // $script:0831180407003174$
                // - In an instant, a wave tall enough to block out the sun rose up. The warriors had to finish the fight and warn everyone else to escape before all was lost.
                return 12;
            case (12, 6):
                // $script:0831180407003175$
                // - Acting as a team, the warriors came together and pressed back against $npcName:23000017$ twice as hard. It was the most intense battle I've ever seen. 
                return 12;
            case (12, 7):
                // $script:0831180407003176$
                // - I'll never forget the moment they finally flipped $npcName:23000017$ over. It was an incredible victory, cut short by the massive tsunami crashing down on us!
                return 12;
            case (12, 8):
                // $script:0831180407003177$
                // - I don't know how long I was out. When I woke up, the sky was clear and the sea was quiet, as if the terror of the previous night was but a dream. It might as well be for those warriors... for they and $npcName:23000017$ were all swept out to sea. 
                return 12;
            case (12, 9):
                // $script:0831180407003178$
                // - What was perhaps the most frenzied battle in history was lost to the tides, with only myself and a few other survivors to retell the story. 
                return 12;
            case (12, 10):
                // $script:0831180407003179$
                // - $npcName:23000017$ has never returned to bother us since that day. I don't know if the tsunami swept it away, or if our heroes taught it a lesson.
                return 12;
            case (12, 11):
                // $script:0831180407003180$
                // - I've been studying turtles in the hopes of finding a clue to where their king went. And now, with my bald head and hunched-up shoulders and craning neck, I almost look like a turtle myself. Heh. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Next,
            (12, 2) => NpcTalkButton.Next,
            (12, 3) => NpcTalkButton.Next,
            (12, 4) => NpcTalkButton.Next,
            (12, 5) => NpcTalkButton.Next,
            (12, 6) => NpcTalkButton.Next,
            (12, 7) => NpcTalkButton.Next,
            (12, 8) => NpcTalkButton.Next,
            (12, 9) => NpcTalkButton.Next,
            (12, 10) => NpcTalkButton.Next,
            (12, 11) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
