using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001026: Raymon
/// </summary>
public class _11001026 : NpcScript {
    internal _11001026(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003483$ 
                // - Sigh...  
                return true;
            case 30:
                // $script:0831180407003486$ 
                // - Everything that happened to us is my fault. I shouldn't have dragged $npcName:11000492[gender:0]$ into it... I was blinded by greed and... he died because of me.  
                switch (selection) {
                    // $script:0831180407003487$
                    // - How did $npcName:11000492[gender:0]$ die?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407003488$
                    // - What kind of deal did you make with $npcName:11000044[gender:0]$?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407003489$ 
                // - Well... It's all because of that blasted caravan attack. Just before $npcName:11000492[gender:0]$ became a suspect, he wanted to go over our alibis. I went to our meeting spot in the $map:02000043$ to meet him. 
                // $script:0831180407003490$ 
                // - $npcName:11000044[gender:0]$'s assassins were waiting for us when I got there. They thought $npcName:11000492[gender:0]$ and I were loose ends, so they were going to get rid of us. 
                // $script:0831180407003491$ 
                // - I escaped, but it was too late for $npcName:11000492[gender:0]$. I never imagined things would go so wrong. 
                return true;
            case 32:
                // $script:0831180407003492$ 
                // - It wasn't a deal so much as extortion. I've been stealing money from Barrota for years. Basic stuff–a redirected delivery here, an extra fee there. 
                // $script:0831180407003493$ 
                // - $npcName:11000044[gender:0]$ found out somehow. If I didn't work with him, he'd have exposed me to the public. 
                switch (selection) {
                    // $script:0831180407003494$
                    // - And what did he want?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407003495$ 
                // - He wanted the supplies for the big court gathering in $map:02000001$. I offered to pay him off, but he said he wasn't interested in money. That's when I realized he was up to something truly dangerous... but it didn't make a difference to me. 
                // $script:0831180407003496$ 
                // - Of course, stealing imperial supplies is a tall order. I needed a man on the inside, and I got it in $npcName:11000492[gender:0]$. He had a reputation for being a straight shooter, but everyone has a price. 
                // $script:0831180407003497$ 
                // - $npcName:11000492[gender:0]$'s mother is sick. I told him I could get her the best medicine money can buy. Better, even. That did the trick. 
                // $script:0831180407003498$ 
                // - I promised $npcName:11000492[gender:0]$ that nobody would get hurt. It was a lie, of course, but desperate men will believe anything to ease their consciences. It wasn't hard to get the caravan route and schedule out of him. 
                // $script:0831180407003499$ 
                // - I delivered the plans to $npcName:11000044[gender:0]$ personally. Met him at $map:02000117$. Him and the lady in the red cloak... I knew then that I'd never be able to live with myself after what I'd done. 
                // $script:0831180407003500$ 
                // - But it was all over... or so I thought. The court was canceled, an earthquake tore up the royal road... All I knew was that I wanted out. 
                switch (selection) {
                    // $script:0831180407003501$
                    // - And how did that go?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0831180407003502$ 
                // - You know darn well how that went. Now $npcName:11000492[gender:0]$ is gone and my life is ruined... 
                return true;
            default:
                return true;
        }
    }
}
