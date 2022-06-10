using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001246: Ishura
/// </summary>
public class _11001246 : NpcScript {
    internal _11001246(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1203181207004692$ 
                // - Hmm? 
                return true;
            case 30:
                // $script:1206021407004794$ 
                // - Ah, $MyPCName$! What a pleasant surprise. 
                switch (selection) {
                    // $script:1206021407004795$
                    // - I have a few questions to ask.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1206021407004796$ 
                // - Certainly. What would you like to know?  
                switch (selection) {
                    // $script:1206021407004797$
                    // - What can you tell me about Arazaad?
                    case 0:
                        Id = 35;
                        return false;
                    // $script:1206021407004798$
                    // - What can you tell me about $npcName:11001231[gender:0]$?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1211024207004974$
                    // - When can we go home?
                    case 2:
                        Id = 38;
                        return false;
                }
                return true;
            case 32:
                // $script:1206021407004799$ 
                // - Sigh... I'd rather not talk about him, but I suppose you need all the information you can get. 
                switch (selection) {
                    // $script:1206021407004800$
                    // - But I thought you and $npcName:11001231[gender:0]$ were friends.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1206021407004801$ 
                // - There was a time long ago that was true, but... well, you know Terrun Calibre's history. I supposed the rift that grew between us was inevitable. The Jibricia value rune magic above all, while the Pelgia prize swordsmanship. And rather than work in harmony, they fight like children. 
                // $script:1206021407004802$ 
                // - From an early age, $npcName:11001231[gender:0]$ had shown an incredible aptitude for the three elements. It wasn't long before the Jibricia took notice of him. Nor did it take long for him to climb to the top of the sect. 
                switch (selection) {
                    // $script:1206021407004803$
                    // - But how did you and $npcName:11001231[gender:0]$ become friends?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1206021407004804$ 
                // - He was Jibricia and I was Pelgia. And though our sects were bitterly opposed to one another, $npcName:11001231[gender:0]$ and I recognized in each other a kindred spirit. Our elders forbade us from meeting, but that didn't dissuade us. We had such big plans. You know, we truly believe we could find a way to end the conflict. 
                // $script:1206021407004805$ 
                // - We would stay up all night, just talking. He was a talented warrior and the strongest of the Eight Blades. Together, I was sure we could really accomplish all the things we used to discuss... 
                // $script:1206021407004806$ 
                // - Even with the passage of time, I still had hope. I dreamed of building a new future for Terrun Calibre with him... 
                // $script:1206021407004807$ 
                // - Of course, my dream was destroyed when he killed Arazaad. He crossed a line from which he could never return. And now, I can't help but wonder if there was some sign I could have missed... 
                return true;
            case 35:
                // $script:1206021407004808$ 
                // - Arazaad was an admirable man. Not only was he the leader of our sect, Pelgia, but as Elder Blade he was the leader of all Terrun Calibre. This was a source of conflict on both sides. All Arazaad wanted was peace. Though the fighting between the two sects began with the elders, in the end it was Arazaad who took the blame. 
                // $script:1206021407004809$ 
                // - Some called Arazaad a hypocrite, but the man was nothing short of an inspiration. Even though $npcName:11001231[gender:0]$ was among the leader of our rival sect, the Jibricia, he still looked up to Arazaad. 
                // $script:1206021407004810$ 
                // - Of course, $npcName:11001231[gender:0]$ was <i>not</i> Arazaad's most trusted student. 
                switch (selection) {
                    // $script:1206021407004811$
                    // - Let me guess, it was you.
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:1206021407004812$ 
                // - Ha! So often did I wish that I were. No, Arazaad's prized student was $npcName:11001230[gender:0]$. 
                switch (selection) {
                    // $script:1206021407004813$
                    // - $npcName:11001230[gender:0]$? Really? I would have never guessed.
                    case 0:
                        Id = 37;
                        return false;
                }
                return true;
            case 37:
                // $script:1206021407004814$ 
                // - I can't blame you, he certainly doesn't act the part. Initially, Arazaad tried to keep $npcName:11001230[gender:0]$ on a tight leash. But the more defiant $npcName:11001230[gender:0]$ became, the more attention he got from Arazaad. 
                // $script:1206021407004815$ 
                // - And now he's the acting Elder Blade of Terrun Calibre. In any case, I've said more than I should have. It wouldn't be right to discuss such things without him here to share his side of the story. 
                return true;
            case 38:
                // $script:1211024207004975$ 
                // - You miss Calibre Island already? Don't fret, I'm sure we'll be able to return... someday. 
                switch (selection) {
                    // $script:1211024207004976$
                    // - Why can't we go back now?
                    case 0:
                        Id = 39;
                        return false;
                }
                return true;
            case 39:
                // $script:1211024207004977$ 
                // - Simply reaching the island requires massive amounts of rune mana, and there isn't much to be found in a place like this. Our only hope of returning is in finding all the pieces of the Wisdom of the Baaz. 
                return true;
            default:
                return true;
        }
    }
}
