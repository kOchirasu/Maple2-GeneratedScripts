using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000008: Green Hood
/// </summary>
public class _11000008 : NpcScript {
    internal _11000008(INpcScriptContext context) : base(context) {
        Id = 50;
        // TODO: RandomPick 50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 1:
                // $script:0831180407000032$ 
                // - What's wrong?
                return true;
            case 50:
                // $script:0831180407000037$ 
                // - Welcome to $map:02000076$. How may I help you?
                switch (selection) {
                    // $script:0831180407000038$
                    // - Sell me on this $map:02000076$ business.
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407000039$
                    // - What happened to the empress's celebration?
                    case 1:
                        Id = 52;
                        return false;
                    // $script:0831180407000040$
                    // - Hey there. I'm new in town.
                    case 2:
                        Id = 53;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407000042$ 
                // - $map:02000076$ used to be the home of archers and craftsmen, all living in a collective. They produced many great works and great hunters, generation after generation.
                // $script:0831180407000043$ 
                // - The Green Hoods formed to protect the village from outside threats to their peace. Their current leader is their fifth, $npcName:11000015[gender:1]$.
                // $script:0831180407000044$ 
                // - Is $npcName:11000015[gender:1]$ the chief of this village? Ha ha, no. Henesys's chief is $npcName:11000001[gender:0]$. $npcName:11000015[gender:1]$'s father and $npcName:11000001[gender:0]$ have been best friends since they were young.
                // $script:0831180407000045$ 
                // - That's why $npcName:11000001[gender:0]$ takes care of $npcName:11000015[gender:1]$ like his own. You know, $npcName:11000015[gender:1]$ doesn't like people talking about her. So, maybe don't tell her about this conversation?
                return true;
            case 52:
                // $script:0831180407000046$ 
                // - I've heard a great earthquake occurred near $map:02000001$, and the empress's court was canceled as a result. I hope the damage isn't too serious. That disaster might also keep $npcName:11000045[gender:0]$ from returning anytime soon.
                // $script:0831180407000047$ 
                // - $npcName:11000045[gender:0]$ won't tolerate anyone trying to take advantage of a chaotic situation. I hope he'll be back soon. We need him more than ever. 
                return true;
            case 53:
                // $script:0831180407000048$ 
                // - You've probably noticed that the Green Hoods are all archers. We're renowned throughout Victoria Island for our marksmanship, and even $npcName:11000045[gender:0]$, the master archer of $map:02000001$, is a Green Hood.
                // $script:0831180407000049$ 
                // - In fact, she taught me everything I know about loosing a bow. If you're interested in archery yourself, I'd suggest paying her a visit next time you're in the capital.
                return true;
            case 54:
                // $script:0831180407000050$ 
                // - Everyone in Maple World dreams of having a house of their own. $npcName:11000001[gender:0]$ is doing what he can to manage the housing lots around the village, but there's only so much land.
                // $script:0831180407000051$ 
                // - If you don't have a house yet, you could settle down in $map:02000076$. $map:02000105$ is also quite nice, and is famous for its beautiful maple trees. There might be some empty lots still available in $map:02000104$ or $map:02000143$ as well. If you're looking for more affordable options, then you can check out the apartments in $map:02000105$ or $map:02000104$.
                // $script:0831180407000052$ 
                // - There are many advantages to owning a house, you know. These days, every home comes with a device that will let you teleport there at anytime from almost anywhere. Let me tell you, it's saved my butt plenty of times after a long day of patrolling the ant tunnels.
                // $script:0831180407000053$ 
                // - And the merchants in $map:02000036$, west of $map:02000023$, have all kinds of interesting furnishings for sale. Decorate your floors, walls, furniture, and yard to create a house that's unique to you. Some merchants will even sell buildings you can place on your lot! When you're ready to buy, go to $map:02000036$ to shop for your house.
                // $script:0831180407000054$ 
                // - If you already have a house, hiring a maid is a good next step. $npcName:11000700[gender:1]$ in $map:02000001$ is an expert on assistants and can definitely help you out. Maybe you should look for a house around $map:02000076$ first.
                return true;
            default:
                return true;
        }
    }
}
