using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001246: Ishura
/// </summary>
public class _11001246 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1203181207004692$
    // - Hmm?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1206021407004794$
                // - Ah, $MyPCName$! What a pleasant surprise.
                switch (selection) {
                    // $script:1206021407004795$
                    // - I have a few questions to ask.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1206021407004796$
                // - Certainly. What would you like to know? 
                switch (selection) {
                    // $script:1206021407004797$
                    // - What can you tell me about Arazaad?
                    case 0:
                        return 35;
                    // $script:1206021407004798$
                    // - What can you tell me about $npcName:11001231[gender:0]$?
                    case 1:
                        return 32;
                    // $script:1211024207004974$
                    // - When can we go home?
                    case 2:
                        return 38;
                }
                return -1;
            case (32, 0):
                // $script:1206021407004799$
                // - Sigh... I'd rather not talk about him, but I suppose you need all the information you can get.
                switch (selection) {
                    // $script:1206021407004800$
                    // - But I thought you and $npcName:11001231[gender:0]$ were friends.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1206021407004801$
                // - There was a time long ago that was true, but... well, you know Terrun Calibre's history. I supposed the rift that grew between us was inevitable. The Jibricia value rune magic above all, while the Pelgia prize swordsmanship. And rather than work in harmony, they fight like children.
                return 33;
            case (33, 1):
                // $script:1206021407004802$
                // - From an early age, $npcName:11001231[gender:0]$ had shown an incredible aptitude for the three elements. It wasn't long before the Jibricia took notice of him. Nor did it take long for him to climb to the top of the sect.
                switch (selection) {
                    // $script:1206021407004803$
                    // - But how did you and $npcName:11001231[gender:0]$ become friends?
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1206021407004804$
                // - He was Jibricia and I was Pelgia. And though our sects were bitterly opposed to one another, $npcName:11001231[gender:0]$ and I recognized in each other a kindred spirit. Our elders forbade us from meeting, but that didn't dissuade us. We had such big plans. You know, we truly believe we could find a way to end the conflict.
                return 34;
            case (34, 1):
                // $script:1206021407004805$
                // - We would stay up all night, just talking. He was a talented warrior and the strongest of the Eight Blades. Together, I was sure we could really accomplish all the things we used to discuss...
                return 34;
            case (34, 2):
                // $script:1206021407004806$
                // - Even with the passage of time, I still had hope. I dreamed of building a new future for Terrun Calibre with him...
                return 34;
            case (34, 3):
                // $script:1206021407004807$
                // - Of course, my dream was destroyed when he killed Arazaad. He crossed a line from which he could never return. And now, I can't help but wonder if there was some sign I could have missed...
                return -1;
            case (35, 0):
                // $script:1206021407004808$
                // - Arazaad was an admirable man. Not only was he the leader of our sect, Pelgia, but as Elder Blade he was the leader of all Terrun Calibre. This was a source of conflict on both sides. All Arazaad wanted was peace. Though the fighting between the two sects began with the elders, in the end it was Arazaad who took the blame.
                return 35;
            case (35, 1):
                // $script:1206021407004809$
                // - Some called Arazaad a hypocrite, but the man was nothing short of an inspiration. Even though $npcName:11001231[gender:0]$ was among the leader of our rival sect, the Jibricia, he still looked up to Arazaad.
                return 35;
            case (35, 2):
                // $script:1206021407004810$
                // - Of course, $npcName:11001231[gender:0]$ was <i>not</i> Arazaad's most trusted student.
                switch (selection) {
                    // $script:1206021407004811$
                    // - Let me guess, it was you.
                    case 0:
                        return 36;
                }
                return -1;
            case (36, 0):
                // $script:1206021407004812$
                // - Ha! So often did I wish that I were. No, Arazaad's prized student was $npcName:11001230[gender:0]$.
                switch (selection) {
                    // $script:1206021407004813$
                    // - $npcName:11001230[gender:0]$? Really? I would have never guessed.
                    case 0:
                        return 37;
                }
                return -1;
            case (37, 0):
                // $script:1206021407004814$
                // - I can't blame you, he certainly doesn't act the part. Initially, Arazaad tried to keep $npcName:11001230[gender:0]$ on a tight leash. But the more defiant $npcName:11001230[gender:0]$ became, the more attention he got from Arazaad.
                return 37;
            case (37, 1):
                // $script:1206021407004815$
                // - And now he's the acting Elder Blade of Terrun Calibre. In any case, I've said more than I should have. It wouldn't be right to discuss such things without him here to share his side of the story.
                return -1;
            case (38, 0):
                // $script:1211024207004975$
                // - You miss Calibre Island already? Don't fret, I'm sure we'll be able to return... someday.
                switch (selection) {
                    // $script:1211024207004976$
                    // - Why can't we go back now?
                    case 0:
                        return 39;
                }
                return -1;
            case (39, 0):
                // $script:1211024207004977$
                // - Simply reaching the island requires massive amounts of rune mana, and there isn't much to be found in a place like this. Our only hope of returning is in finding all the pieces of the Wisdom of the Baaz.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Next,
            (34, 2) => NpcTalkButton.Next,
            (34, 3) => NpcTalkButton.Close,
            (35, 0) => NpcTalkButton.Next,
            (35, 1) => NpcTalkButton.Next,
            (35, 2) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.SelectableDistractor,
            (37, 0) => NpcTalkButton.Next,
            (37, 1) => NpcTalkButton.Close,
            (38, 0) => NpcTalkButton.SelectableDistractor,
            (39, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
