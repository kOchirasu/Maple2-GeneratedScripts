using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001203: Kiro Karr
/// </summary>
public class _11001203 : NpcScript {
    internal _11001203(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1017225707004220$ 
                // - Please don't interrupt me while I am praying. 
                return true;
            case 30:
                // $script:1017225707004222$ 
                // - <i>Shalua le mashalua...</i>
I am conducting an important <b>rite</b>. Please be quiet. 
                switch (selection) {
                    // $script:1017225707004223$
                    // - What's the deal with this rite?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1017225707004224$ 
                // - All around the world, there exist forces of darkness which threaten the peace. Few are brave enough to confront them. And so those who do are branded heroes. 
                // $script:1017225707004225$ 
                // - $npcName:11001201$, having attained enlightenment and seen the truth of the world, wants to help such heroes through prayer. And so, she and her successor, $npcName:11001202$, have embarked on a holy pilgrimage. 
                // $script:1019105307004236$ 
                // - It would be naïve to think that prayer will miraculously vanquish all of the evil in the world. But there is no denying the restorative power of prayer. Such is the purpose of their pilgrimage, to empower heroes to resist evil. 
                switch (selection) {
                    // $script:1019105307004237$
                    // - I've never heard of good Inakimos.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1017225707004227$ 
                // - Sadly, your prejudice is not entirely unfounded.
We too have heard many stories of evil Inakimos.
But me, and the rest of $npcName:11001201$'s followers are not like them. Our people follow a different faith. We have walked a different path. 
                // $script:1017225707004228$ 
                // - We understand why the rest of the world looks at us with some suspicion, but we want nothing more than to do good for the world, and to make up for the wrongs of other Inakimos. 
                switch (selection) {
                    // $script:1017225707004229$
                    // - That's great and all, but how does that help with the bad Inakimos?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1017225707004230$ 
                // - We're deeply ashamed of our malevolent kin. We wish to stop their wrongdoing as badly as you. But ever since $npcName:11001201$ was exiled from their order for confronting Myuteka Rabo, they have treated us as enemies. 
                // $script:1017225707004231$ 
                // - Besides, we cannot raise a hand against our own kind. We must help them to understand the error of their ways and guide them to righteous path. Even if it is a hopeless endeavor, we must at least try. 
                switch (selection) {
                    // $script:1017225707004232$
                    // - Exiled? What's the deal with Inakimo Karr?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1017225707004233$ 
                // - $npcName:11001201$ was once the most trusted priest of Myuteka Rabo's cult. But he was not blind. He began to question Myuteka's evil ambitions, and was summarily exiled from Myuteka's order. 
                // $script:1017225707004234$ 
                // - With a few loyal followers in tow, he set off upon a journey to learn about the world as it really was, and not as Myuteka preached. It was a perilous journey was perilous, but <font color="#ffd200">$npcName:11001201$</font> persisted. In the end, he found enlightenment wrote a<font color="#ffd200">new doctrine</font> entirely of his own. 
                // $script:1017225707004235$ 
                // - $npcName:11001201$ was devastated to learn of the evil done in the name of Myuteka Rabo's faith. And thus began our pilgrimage. We may unable to confront our kin, but we hope by atoning for their sins to one day redeem ourselves in the eyes of the world. 
                return true;
            default:
                return true;
        }
    }
}
